# Mega-Sena Python Code

Este repositório contém um script em Python que gera números aleatórios simulando o sorteio da Mega-Sena. O código garante que os números gerados são únicos e estão dentro da faixa esperada.

## Descrição

O script gera 6 números aleatórios entre 1 e 60, garantindo que todos os números sejam únicos, como no sorteio oficial da Mega-Sena. Ele utiliza um conjunto (`set`) para garantir que não haja duplicatas entre os números gerados.

## Como Funciona

1. Um conjunto vazio é criado para armazenar os números.
2. Números aleatórios entre 1 e 60 são gerados e adicionados ao conjunto.
3. O processo continua até que 6 números únicos sejam gerados.
4. O conjunto é convertido em uma lista e impresso no console.

## Exemplo de Uso

Para rodar o script, simplesmente execute o seguinte comando no terminal:

```bash
python mega_sena.py
```

### Exemplo de Saída:

```
[12, 23, 45, 30, 9, 58]
```

Cada vez que o script é executado, ele gera um novo conjunto de 6 números aleatórios.

## Requisitos

- Python 3.x

## Como Contribuir

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
