class Musica:
    def __init__(self, titulo, artista, album):
        self._titulo = titulo
        self._artista = artista
        self._album = album

    def get_titulo(self):
        return self._titulo

    def get_artista(self):
        return self._artista

    def get_album(self):
        return self._album

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_artista(self, artista):
        self._artista = artista

    def set_album(self, album):
        self._album = album

    def to_string(self):
        return f"Título: {self._titulo}, Artista: {self._artista}, Álbum: {self._album}"


class PlayList:
    def __init__(self, nome, descricao):
        self._nome = nome
        self._descricao = descricao
        self._musicas = []

    def get_nome(self):
        return self._nome

    def get_descricao(self):
        return self._descricao

    def set_nome(self, nome):
        self._nome = nome

    def set_descricao(self, descricao):
        self._descricao = descricao

    def inserir(self, musica):
        if isinstance(musica, Musica):
            self._musicas.append(musica)
        else:
            raise TypeError("O objeto inserido deve ser uma instância da classe Musica")

    def listar(self):
        return [musica.to_string() for musica in self._musicas]

    def to_string(self):
        return f"PlayList: {self._nome}, Descrição: {self._descricao}, Número de músicas: {len(self._musicas)}"


# Testando as classes Musica e PlayList
musica1 = Musica("Bohemian Rhapsody", "Queen", "A Night at the Opera")
musica2 = Musica("Stairway to Heaven", "Led Zeppelin", "Led Zeppelin IV")
musica3 = Musica("Imagine", "John Lennon", "Imagine")

playlist = PlayList("Clássicos do Rock", "Uma coleção das melhores músicas de rock de todos os tempos")
playlist.inserir(musica1)
playlist.inserir(musica2)
playlist.inserir(musica3)

print(playlist.to_string())
print("Músicas na playlist:")
for musica in playlist.listar():
    print(musica)
