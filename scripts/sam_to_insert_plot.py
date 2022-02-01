import sys
import pysam

from Bio import SeqIO

filename = sys.argv[1]
reference_filename = sys.argv[2]

contig_name_to_size=dict()

reference_contigs = SeqIO.parse(open(reference_filename),'fasta')
for reference_contig in reference_contigs:
    contig_name_to_size[str(reference_contig.id)] = len(reference_contig.seq)

#load reference_filename and compute the contig lengths

forward_inserts_by_contig=dict()
reverse_inserts_by_contig=dict()

# Based on https://samtools.github.io/hts-specs/SAMv1.pdf

samfile = pysam.AlignmentFile(filename)

total_reads=0
total_mapped=0

for read in samfile:
    total_reads = total_reads+1
#    print(dir(read))

    if( not( read.is_unmapped ) ):   #if it's mapped
        total_mapped = total_mapped+1
        contig_name = read.reference_name
        if contig_name not in forward_inserts_by_contig.keys(): forward_inserts_by_contig[contig_name]=dict()
        if contig_name not in reverse_inserts_by_contig.keys(): reverse_inserts_by_contig[contig_name]=dict()

        
        position = read.reference_start+1 # The first position that consumes a reference. Add 1 so it is 1 based not 0 based.
        rc_position = read.reference_start+1
        cigarLine=read.cigar;

        cigar_number=0
        for (cigarType,cigarLength) in cigarLine:
            cigar_number=cigar_number+1


        #if(cigarType == 4) and cigar_number==1: # Soft clipped at the start
        #    position=position+cigarLength
            if(  cigarType == 0): #match
                rc_position=rc_position+cigarLength
                
            #elif(cigarType == 1): #insertions
            elif(cigarType == 2): #deletion
                rc_position=rc_position+cigarLength
            elif(cigarType == 3): #skip
                rc_position=rc_position+cigarLength
            #elif(cigarType == 4): #soft clipping
            #    print(cigarLength)
            #elif(cigarType == 5): #hard clipping
            #elif(cigarType == 6): #padding
            elif(cigarType == 7): #sequence match
                rc_position=rc_position+cigarLength
            elif(cigarType == 8): #sequence mismatch
                rc_position=rc_position+cigarLength
            #else:
            #    print "Wrong CIGAR number";
            #    sys.exit(1);





            
            #try:
            #if(cigarType == 4) and cigar_number==1: # Soft clipped at the start
            #    position=position+cigarLength
                #if(  cigarType == 0): #match                  
                #elif(cigarType == 1): #insertions
                #elif(cigarType == 2): #deletion
                #elif(cigarType == 3): #skip
                #elif(cigarType == 4): #soft clipping
                #    print(cigarLength)
                #elif(cigarType == 5): #hard clipping
                #elif(cigarType == 6): #padding
                #else:
                #    print "Wrong CIGAR number";
                #    sys.exit(1);
           # except:
           #     print "Problem";

        if read.flag==0:
            forward_inserts = forward_inserts_by_contig[contig_name]
            if position not in forward_inserts.keys(): forward_inserts[position]=0
            forward_inserts[position]=forward_inserts[position]+1
                # This need to look at the cigar string...
        elif read.flag==16:
            reverse_inserts = reverse_inserts_by_contig[contig_name]
            if rc_position not in reverse_inserts.keys(): reverse_inserts[rc_position]=0
            reverse_inserts[rc_position]=reverse_inserts[rc_position]+1


#        if rc_position>1506658 and rc_position<1506716:
#            print(rc_position)
#            print(read)

#print(max(forward_inserts.keys()))
#print(max(reverse_inserts.keys()))

insertion_sites_by_contig = dict()

for contig_name in forward_inserts_by_contig:
    if contig_name not in insertion_sites_by_contig.keys(): insertion_sites_by_contig[contig_name]=0
    
    insert_plot_file = open(contig_name + '.insert_plot','w+')
    forward_inserts = forward_inserts_by_contig[contig_name]
    reverse_inserts = reverse_inserts_by_contig[contig_name]
                
    for i in range(1,max(forward_inserts.keys())+1):
        insertion_site=False
        if i in forward_inserts.keys():
            insertion_site=True
            insert_plot_file.write(str(forward_inserts[i]))
        else: insert_plot_file.write('0')

        insert_plot_file.write(' ')
            
        if i in reverse_inserts.keys():
            insertion_site=True
            insert_plot_file.write(str(reverse_inserts[i]))
        else: insert_plot_file.write('0')

        if insertion_site: insertion_sites_by_contig[contig_name]=insertion_sites_by_contig[contig_name]+1

        insert_plot_file.write('\n')

print("Total Reads\t" + str(total_reads))
print("Total Mapped\t" + str(total_mapped))
print("Percentage Mapped\t" + str((100*total_mapped)/total_reads))

total_uis=0
total_contig_length=0
for contig_name in insertion_sites_by_contig.keys():
    print("Statistics for contig\t" + contig_name)
    
    print("Unique insertion sites\t" + str(insertion_sites_by_contig[contig_name]))
    total_uis=total_uis+insertion_sites_by_contig[contig_name]
    
    print("Contig length\t" + str(contig_name_to_size[contig_name]))
    total_contig_length=total_contig_length+contig_name_to_size[contig_name]
    
    print("Contig length / UIS\t" + str(contig_name_to_size[contig_name]/insertion_sites_by_contig[contig_name]))

print("\n\nGrand total")
print("Total Unique insertion sites\t" + str(total_uis))
print("Total contig lengths\t" + str(total_contig_length))
print("Total contig length / UIS\t" + str(total_contig_length/total_uis))
