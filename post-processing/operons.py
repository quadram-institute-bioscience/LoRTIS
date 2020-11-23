# An operon is a list of genes thrL, thrA, thrC are the same operon but but yaaX since yaaA is on the reverse strand
# For now we can output the list of operons as a look up table.
from Bio import SeqIO

gene2operon = dict()

site2geneNamesPositive = dict() # For each site on the positive strand, keep a list of the genes which cover it
site2geneNamesNegative = dict() # For each site on the positive strand, keep a list of the genes which cover it

gene2start = dict()
gene2end = dict()

lengthOfPrimeRegion=50


for record in SeqIO.parse("/home/martin/Quadram/bio-tradis-data/cp009273.embl", "embl"):
    print(record)

    features = record.features
    for feature in features:
        qualifiers = feature.qualifiers
        location = feature.location
        
        locationStart = location.start
        locationEnd = location.end
        
        geneName = 'unknown'

        isPrime=False
        geneNames = None
        if 'gene' in qualifiers.keys():
            geneNames = qualifiers['gene']

            for geneName in geneNames:
                if location.strand==1:
                    if '5prime' in geneName:
                        locationStart = locationEnd-lengthOfPrimeRegion
                    elif '3prime' in geneName:
                        locationEnd = locationStart+lengthOfPrimeRegion
                elif location.strand==-1:
                    if '5prime' in geneName:
                        locationEnd = locationStart+lengthOfPrimeRegion
                    elif '3prime' in geneName:
                        locationStart = locationEnd-lengthOfPrimeRegion
                
                gene2start[geneName] = locationStart
                gene2end[geneName] = locationEnd
                
        
        for i in range(locationStart,locationEnd):
            if location.strand==1:
                if i not in site2geneNamesPositive.keys(): site2geneNamesPositive[i] = set()

                if geneNames is not None:
                    if type(geneNames)==list:
                        for geneName in geneNames:
                            site2geneNamesPositive[i].add(geneName)
                    else:
                        site2geneNamesPositive[i].add(geneNames)

            if location.strand==-1:
                if i not in site2geneNamesNegative.keys(): site2geneNamesNegative[i] = set()

                if geneNames is not None:
                    if type(geneNames)==list:
                        for geneName in geneNames:
                            site2geneNamesNegative[i].add(geneName)
                    else:
                        site2geneNamesNegative[i].add(geneNames)


def outputOperons(site2geneNames1,site2geneNames2,strandName):
    lastOperonEnd=0
    operonStart=0
    operonGenes=dict()

    for i in range(0,max(site2geneNames1.keys())):
        if i not in site2geneNames2.keys(): site2geneNames2[i] = set()

        if i in site2geneNames1.keys():
            geneNames = site2geneNames1[i]

            foundGeneNotPrime = False
            for geneName in geneNames:
                if 'prime' not in geneName:
                    foundGeneNotPrime=True
            
            otherGeneNames = site2geneNames2[i]

            foundOtherGeneNotPrime = False
            for otherGeneName in otherGeneNames:
                if 'prime' not in otherGeneName:
                    foundOtherGeneNotPrime=True

            if geneNames is None or len(geneNames)==0 or (site2geneNames2[i] is not None and len(site2geneNames2[i])>0 and foundOtherGeneNotPrime==True and foundGeneNotPrime==True): # Found the end of an operon?
                
                if len(operonGenes.keys())>0:
                    printedHeader=False
                    genesAlreadySeen = set()
                    sites = sorted(operonGenes.keys())

                    seenGeneParts = set()
                    allowedGeneNames = set()
                    allowedGenes = set()
                    for site in sites:
                        operonGeneNames = operonGenes[site]
                        for geneName in operonGeneNames:
                            seenGeneParts.add(geneName)
                            if '3prime' in geneName:
                                allowedGeneNames.add(geneName[:-8])

                    for allowedGeneName in allowedGeneNames:
                        if allowedGeneName in seenGeneParts: # and allowedGeneName+'__3prime' in seenGeneParts and allowedGeneName+ '__5prime' in seenGeneParts:
                            allowedGenes.add(allowedGeneName)
                    
                    
                    for site in sites:
                        operonGeneNames = operonGenes[site]
                        for geneName in operonGeneNames:
                            if geneName not in genesAlreadySeen and geneName in allowedGenes:
                                if not printedHeader:
                                    operonStart=9999999999999999
                                    operonEnd=-1
                                    for site in sites:
                                        operonGeneNames = operonGenes[site]
                                        for myGeneName in operonGeneNames:
                                            if myGeneName + '__3prime' in gene2start.keys() and gene2start[myGeneName + '__3prime']<operonStart:operonStart=gene2start[myGeneName + '__3prime']
                                            if myGeneName + '__5prime' in gene2start.keys() and gene2start[myGeneName + '__5prime']<operonStart:operonStart=gene2start[myGeneName + '__5prime']

                                            if myGeneName + '__3prime' in gene2end.keys() and gene2end[myGeneName + '__3prime']>operonEnd:operonEnd=gene2end[myGeneName + '__3prime']
                                            if myGeneName + '__5prime' in gene2end.keys() and gene2end[myGeneName + '__5prime']>operonEnd:operonEnd=gene2end[myGeneName + '__5prime']

                                    print('\n\nOperon start:' + str(operonStart) + ' end:' + str(operonEnd))
                                    lastOperonEnd = operonEnd
                                    printedHeader=True

                                if geneName + "__5prime" in gene2start.keys(): print(strandName + geneName + "__5prime [" + str(gene2start[geneName + "__5prime"]) + ":" + str(gene2end[geneName + "__5prime"]) + "]")
                                print(strandName + geneName + " [" + str(gene2start[geneName]) + ":" + str(gene2end[geneName]) + "]")
                                if geneName + "__3prime" in gene2start.keys(): print(strandName + geneName + "__3prime [" + str(gene2start[geneName + "__3prime"]) + ":" + str(gene2end[geneName + "__3prime"]) + "]")
                                genesAlreadySeen.add(geneName)

                    # if printedHeader: print('stop\n\n')
                    operonStart=i
                    operonGenes=dict()
                else:
                    operonStart = i
            else:
                if i not in operonGenes.keys(): operonGenes[i] = set()
                for geneName in geneNames:
                    operonGenes[i].add(geneName)

    if max(site2geneNames1.keys()) - operonStart > 10:
        printedHeader=False

        genesAlreadySeen=set()
        sites = sorted(operonGenes.keys())
        for site in sites:
            operonGeneNames = operonGenes[site]
            if geneName not in genesAlreadySeen:
                if not printedHeader:
                    print('Final operon start:' + str(operonStart) + ' end:' + str(max(site2geneNames1.keys())+1))
                    printedHeader=True
                print(strandName + geneName + " [" + str(site) + "]")
                genesAlreadySeen.add(geneName)

        if printedHeader: print('stop\n\n')
        
outputOperons(site2geneNamesPositive,site2geneNamesNegative,'+')
outputOperons(site2geneNamesNegative,site2geneNamesPositive,'-')


