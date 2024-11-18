// Interação com a sidebar
const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});

// Função para inicializar uma tabela DataTable com configurações padrão
function inicializarTabela(tabela){
  return new DataTable(tabela, {

    //Traduz o datatable e retira o texto da lista de paginas
    language: {
      url: "https://cdn.datatables.net/plug-ins/1.11.3/i18n/pt_br.json",
      lengthMenu: "Exibir _MENU_ "
    },

    // Define o tipo de paginação
    pagingType: "simple_numbers",

    //Tira a ordenção default da primeira coluna
    order: [],

    // Deixa as tabelas responsivas
    responsive: true
    
  })
}

// Inicializa as tabelas ultlizando a configuração padrão da função datatables
let colaboradores = inicializarTabela('#usuarios')


// Inicializa os alertas personalizados
document.addEventListener('DOMContentLoaded', function () {
  var toastElList = [].slice.call(document.querySelectorAll('.toast'));
  toastElList.forEach(function (toastEl) {
      var toast = new bootstrap.Toast(toastEl);
      toast.show();
  });
});