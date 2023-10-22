### Instalações necessárias
Para utilizar a aplicação é necesário instalar alguns recursos em sua máquina

#### Instalação do Docker Desktop:

Entre em https://www.docker.com/products/docker-desktop/ e siga as instruções de instalação para o seu sistema operacional.

#### Instalação do Git:

Entre em https://git-scm.com/ e sigas as intruções de instalação para seu sistema operacional.

Este passo é necessário apenas caso o usuário queira utilizar comandos git no terminal.

#### Rodando o projeto:

Após é necessário que baixe este repositório em sua máquina e isso pode ser feito de duas maneiras:

* Via comando Git - abra seu terminal na pasta de onde quer baixar o projeto e digite o comando:

```bash
git clone https://github.com/paulomoreiradev/mycollege --config core.autocrlf=input
```

Assim, o repositório sera baixado na pasta de destino escolhida.


#### Rodando o projeto:

Abra o Docker Desktop e siga os primeiros passos dados pelo programa. 

Abra a pasta do projeto e clique com o botão direito do mouse em uma área vazia da pasta. Clique na opção abrir no terminal e rode o seguinte comando:

```bash
docker compose up -d
```

Após isso o Docker criará uma imagem virtual onde estará rodando o site. Na sessão "Containers" do Docker Desktop, você encontrará o container onde o projeto estará rodando. Clique em "mycollege" e em seguida no número "8000:8000⁠" em baixo da primeira opção. E o site abrirá no seu navegador padrão.

**Admin user**

