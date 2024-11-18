from django.shortcuts import render, redirect, get_object_or_404
from usuarios.models import Usuario
from django.contrib import messages


# Lista os usuarios cadastrados
def listaUsuarios(request):
    usuarios = Usuario.objects.all().order_by("nome")
    perfis = Usuario._meta.get_field("perfil").choices
    return render(request, "usuarios/listar.html", {"usuarios": usuarios, "perfis": perfis})

# Cadastra usuário
def novoUsuario(request):
    # Verifica se a requisição é do tipo POST
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")
        telefone = request.POST.get("telefone")
        perfil = request.POST.get("perfil")

        # Tratamento de erros, verifica se o registro foi cadastrado com sucesso e exibe uma mensagem
        try:
            cadastrar_usurio = Usuario(
                nome=nome,
                email=email,
                cpf=cpf,
                telefone=telefone,
                perfil=perfil,
            )

            # Salva o usuario no banco de dados
            cadastrar_usurio.save()
            messages.success(request, "Usuario cadastrado com sucesso!")

        except Exception as e:
            messages.error(request, f"Erro ao cadastrar o usuário: {str(e)}")

        # Redireciona para a lista de usuários
        return redirect("lista_usuarios")

# Edita os usuarios cadastrados
def editaUsuario(request, usuario_id):
    # A função get_object_or_404 possui dois argumentos (TABELA DO BANCO E ID)
    # Caso a função encontre o ID na tabela o registro é retornado, caso o ID não seja encontrado ocorrera um erro 404
    usuario = get_object_or_404(Usuario, pk=usuario_id)

    # Verifica se a requisição é do tipo POST
    if request.method == "POST":
        # Recupera os valores do formulário de edição
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")
        telefone = request.POST.get("telefone")

        try:
            usuario.



    perfis = Usuario._meta.get_field("perfil").choices
    return render(request, "usuarios/editar.html", {"usuario": usuario, "perfis": perfis})

