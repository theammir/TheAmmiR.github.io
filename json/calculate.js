$(document).ready(function(){
  console.log("ready")
  $.getJSON("json/payments.json", {}, function(json) {
    let data = json.data;
    console.log(data);

    $.each(data.salary, function(k, v) {
      $("#order-table").append($("<tr>")
        .append($("<td>")
          .text(k))
        .append($("<td>")
          .text(v + "$"))
        .append($("<td>")
          .text(data.lance_status[k])));

    });
  });

});