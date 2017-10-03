$(document).on("click", function(e){
    if($(e.target).is("#loan_btn")){
      $("#loan_div").toggle();
    }
});

$(document).on("click", function(e){
    if($(e.target).is("#return_btn")){
      $("#return_div").toggle();
    }
});

function loan_post() {
  var object = $("#loan_object").val();
  var name = $("#loan_name").val();
  console.log("object", object, "name", name);
  $.ajax({
    url: '/loan',
    dataType: 'json',
    type: 'post',
    contentType: 'application/json',
    data: JSON.stringify( { "object": $('#loan_object').val(), "name": $('#loan_name').val() } ),
    processData: false,
    success: function( data, textStatus, jQxhr ){
        console.log(data.data);
    },
    error: function( jqXhr, textStatus, errorThrown ){
        console.log( errorThrown );
    }
});
  console.log("envio")
};