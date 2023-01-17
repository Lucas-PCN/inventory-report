from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    nome_do_produto = "Iphone"
    nome_da_empresa = "Apple"
    data_de_fabricacao = "10/10/2022"
    data_de_validade = "undefined"
    numero_de_serie = "LXS123456"
    instrucoes_de_armazenamento = "armazenar em local seco"

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert product.id == id
    assert product.nome_do_produto == nome_do_produto
    assert product.nome_da_empresa == nome_da_empresa
    assert product.data_de_fabricacao == data_de_fabricacao
    assert product.data_de_validade == data_de_validade
    assert product.numero_de_serie == numero_de_serie
    assert product.instrucoes_de_armazenamento == instrucoes_de_armazenamento
