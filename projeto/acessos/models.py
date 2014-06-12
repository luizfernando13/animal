from django.db import models

# Create your models here.
class Grupo(models.Model):
    '''
        @Grupo: Classe criada apenas para geracao das permissoes sobre elas
    '''
#NAO CRIAR PERMISSAO INICIADOS COM A PALAVRA "CAN"
    class Meta:
        permissions = (
            ("criar_grupo", "Pode Adicionar Grupo"),
            ("editar_grupo", "Pode Editar Grupo"),
            ("ver_grupo", "Pode ver Grupo"),
            ("inativar_grupo", "Pode inativar Grupo"),
        )

class Permissao(models.Model):
    '''
        @Grupo: Classe criada apenas para geracao das permissoes sobre elas
    '''
#NAO CRIAR PERMISSAO INICIADOS COM A PALAVRA "CAN"
    class Meta:
        permissions = (
            ("adicionar_permissao_usuario", "Pode adicionar permissao Usuario"),
            ("remover_permissao_usuario", "Pode remover permissao Usuario"),
            ("ver_permissao_usuario", "Pode ver permissao Usuario"),            

            ("adicionar_permissao_grupo", "Pode adicionar permissao Grupo"),
            ("remover_permissao_grupo", "Pode remover permissao Grupo"),
            ("ver_permissao_grupo", "Pode ver permissao Grupo"),




        )