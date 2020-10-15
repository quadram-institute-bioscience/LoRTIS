# An operon is a list of genes thrL, thrA, thrC are the same operon but but yaaX since yaaA is on the reverse strand
# For now we can output the list of operons as a look up table.
from Bio import SeqIO

gene2operon = dict()

site2geneNamesPositive = dict() # For each site on the positive strand, keep a list of the genes which cover it
site2geneNamesNegative = dict() # For each site on the positive strand, keep a list of the genes which cover it



for record in SeqIO.parse("/home/martin/Downloads/cp009273.embl", "embl"):
    print(record)

    features = record.features
    for feature in features:
        qualifiers = feature.qualifiers
        geneName = 'unknown'

        geneNames = None
        if 'gene' in qualifiers.keys():
            geneNames = qualifiers['gene']

        location = feature.location

        
        for i in range(location.start,location.end):
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
    operonStart=0
    operonGenes=set()

    for i in range(0,max(site2geneNames1.keys())):
        if i not in site2geneNames2.keys(): site2geneNames2[i] = set()

        if i in site2geneNames1.keys():
            geneNames = site2geneNames1[i]

            if geneNames is None or len(geneNames)==0 or (site2geneNames2[i] is not None and len(site2geneNames2[i])>0): # Found the end of an operon?
                if len(operonGenes)>0:
                    print(strandName + ' operon start:' + str(operonStart) + ' end:' + str(i+1))

                    for operonGene in operonGenes:
                        print('    gene:' + operonGene)

                    operonStart=i
                    operonGenes=set()
                else:
                    operonStart = i
            else:
                for geneName in geneNames:
                    operonGenes.add(geneName)

    if max(site2geneNames1.keys()) - operonStart > 10:
        print('Final operon start:' + str(operonStart) + ' end:' + str(max(site2geneNames1.keys())+1))

        for operonGene in operonGenes:
            print('    gene:' + operonGene)




outputOperons(site2geneNamesPositive,site2geneNamesNegative,'Positive')
outputOperons(site2geneNamesNegative,site2geneNamesPositive,'Negative')


