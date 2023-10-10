# Ferramenta que verifica se algum bucket sensível foi indexado pelo buscador bing.

A ferramenta verifica se buckets sensíveis da amazon S3 estão indexados no bing. Uma lista de nomes de buckets devem estar no arquivo "buckets.txt" para serem analisados, o script consulta a API do bing, verificando indexação usando URLs específicas do bucket e do domínio s3.amazonaws.com. Para cada bucket, o código exibe um aviso se estiver indexado.

# Tutorial de uso:

1) Inserir a api key do bing na variavel "api_key" do arquivo "check-buckets-indexed-by-bing.py".
2) `python3 check-buckets-indexed-by-bing.py`

# Demonstração:

![image](https://github.com/david-botelho-mariano/check-buckets-indexed-by-bing/assets/48680041/becec151-e858-4b1c-914f-ddb8d0383b37)
