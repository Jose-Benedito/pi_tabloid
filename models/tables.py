from website import db

"""
    Tabela de estabelecimentos
"""
class Estabelecimento(db.Model):
    __tablename__: "estabelecimentos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True)

    """
        Campos obrigatórios:
            - nome
    """
    def __init__(self, nome) -> None:
        self.nome = nome

    def __repr__(self) -> str:
        return "<Estabelecimento %r>" % self.nome



"""
    Tabela de endereço
        - Cada Estabelecimento 'tem' um endereço
"""
class Endereco(db.Model):
    __tablename__: "endereco"

    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(20))
    cidade = db.Column(db.String(20))
    endereco = db.Column(db.String(100), unique=True,)
    numero = db.Column(db.Integer)

    estabelecimento_id = db.Column(db.Integer, db.ForeignKey("estabelecimento.id"))
    estabelecimento = db.relationship('Estabelecimento', foreign_keys=estabelecimento_id)

    """
        Campos obrigatórios:
            - estado 
            - cidade 
            - endereco 
            - numero 
            - estabelecimento_id
    """
    def __init__(self, estado, cidade, endereco, numero, estabelecimento_id) -> None:
        self.estado = estado
        self.cidade = cidade
        self.endereco = endereco
        self.numero = numero
        self.estabelecimento_id = estabelecimento_id
    
    def __repr__(self) -> str:
        return "<Endereco %r>" % self.endereco




"""
    Tabela de contato
        - Cada Estabelecimento 'tem' um contato
"""
class Contato(db.Model):
    __tablename__: "contato"
    id = db.Column(db.Integer, primary_key=True)
    ddd = db.Column(db.Integer)
    telefone = db.Column(db.String(9), unique=True,)
    email = db.Column(db.String(100), unique=True,)

    estabelecimento_id = db.Column(db.Integer, db.ForeignKey("estabelecimento.id"))
    estabelecimento = db.relationship('Estabelecimento', foreign_keys=estabelecimento_id)

    """
        Campos obrigatórios:
            - id 
            - ddd 
            - telefone 
            - estabelecimento_id
    """
    def __init__(self, id, ddd, telefone, estabelecimento_id) -> None:
        self.id = id
        self.ddd = ddd
        self.telefone = telefone
        self.estabelecimento_id = estabelecimento_id

    def __repr__(self) -> str:
        return "<Contato %r>" % self.telefone



"""
    Tabela de rede_social
        -Cada contato 'tem' uma rede_social
"""
class RedeSocial(db.Model):
    __tablename__: "rede_social"
    id = db.Column(db.Integer, primary_key=True)
    facebook = db.Column(db.String(100), unique=True,)
    instagran = db.Column(db.String(100), unique=True,)
    whatsapp = db.Column(db.String(20), unique=True,)
    twitter = db.Column(db.String(100), unique=True,)

    contato_id = db.Column(db.Integer, db.ForeignKey("contato.id"))
    contato = db.relationship('Contato', foreign_keys=contato_id)

    """
        Campos Obrigatórios
            - contato_id
    """
    def __init__(self, contato_id) -> None:
        self.contato_id = contato_id
    
    def __repr__(self) -> str:
        return ""

"""
    Tabela Itens 
        - Cada Estabelecimento 'tem' vários itens
"""
class Itens(db.Model):
    __tablename__: "itens"
    id = db.Column(db.Integer, primary_key=True)
    tipo_item = db.Column(db.String(50))
    nome_item = db.Column(db.String(100))
    marca_item = db.Column(db.String(100))
    volume_tipo = db.Column(db.String(100))
    volume = db.Column(db.String(100))
    qtd_maxima = db.Column(db.Boolean)
    data_fim_promocao = db.Column(db.DateTime)
    foto = db.Column(db.LargeBinary)

    estabelecimento_id = db.Column(db.Integer, db.ForeignKey("estabelecimento.id"))
    estabelecimento = db.relationship('Estabelecimento', foreign_keys=estabelecimento_id)

    """
        Campos obrigatórios
            - tipo_item 
            - nome_item 
            - marca_item 
            - volume_tipo 
            - volume 
            - qtd_maxima 
            - data_fim_promocao 
            - estabelecimento_id

    """
    def __init__(self, tipo_item, nome_item, marca_item, volume_tipo, volume, qtd_maxima, data_fim_promocao, estabelecimento_id) -> None:
        self.tipo_item = tipo_item
        self.nome_item = nome_item
        self.marca_item = marca_item
        self.volume_tipo = volume_tipo
        self.volume = volume
        self.qtd_maxima = qtd_maxima
        self.data_fim_promocao = data_fim_promocao
        self.estabelecimento_id = estabelecimento_id


    def __repr__(self) -> str:
        return "<Nome Item %r>" % self.nome_item