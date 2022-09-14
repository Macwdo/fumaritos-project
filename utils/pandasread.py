def data_files(name):
    txt = open(name, 'r')
    document = txt.read()
    document_list = document.split("\n")
    new = [i.replace('  ', '-').split("-") for i in document_list]
    trt = []
    for i in range(len(new)):
        new_arr = [x for x in new[i] if x != '']
        trt.append(new_arr)
    return trt


produtos = data_files('produtos.txt')
vendidos = data_files('vendidos.txt')

def create_product(produtos,):
    for i in 