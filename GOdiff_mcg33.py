#Extracting the contents of the GO0003723.genelist & creating a dictionary
GO_data = open("GO0003723.genelist")
GO_terms = GO_data.readlines()

genelist_dict = {}

for line in GO_terms:
    line = line.rstrip ("\n") #Removes space between the columns 
    line = line.split("\t") #Splits individual elements using by a tab    
    gene_name = line[3]
    gene_desc = line[4] 
    genelist_dict [gene_name] = gene_desc #Storing the gene name (key) and description (value) in a dictionary     
    
#Extracting the contents of diffexp.tsv & creating a second dictionary
diff_data = open("diffexp.tsv")
diff_exp = diff_data.readlines()

pvalue_dict = {}

for line in diff_exp:
    line = line.split("\t")
    diff_gene_name = line[0]
    diff_gene_P = line[4]   
    pvalue_dict [diff_gene_name] = diff_gene_P #Storing the gene name (key) and P-value (value)
    
#Outputting results of differently expressed genes also found in "GO0003723.genelist" to "GOdiff_mcg33.out.txt"

output_file = open("GOdiff_mcg33.out.txt", "w")
for key in genelist_dict:
    if key in pvalue_dict:
        output_file.write(str(key) + "\t" + genelist_dict.get(key) + "\t" + pvalue_dict.get(key) + "\n")
output_file.close()

#Printing the name of the gene with the lowest P value to the terminal
output_file = open("GOdiff_mcg33.out.txt")
output_content = output_file.read()
output_content = output_content.split("\n")

output_file_dict = {}

for line in output_content:
    line = line.split("\t") 
    if len(line) > 2:
        gene_name = line[0]
        p_value = line[2]       
        output_file_dict[gene_name] = float(p_value)
key_min = min(output_file_dict.keys(), key=output_file_dict.get)
print(key_min)
    
        
