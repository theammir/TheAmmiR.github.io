$(document).ready(function(){
  console.log("ready")
  $.getJSON("json/payments.json", {}, function(json) {
    let data = json.data;
    let actual_sum = 0
    let theory_sum = 0
    let owe_sum = 0
    console.log(data);

    $.each(data.salary, function(k, v) {
      let status_color = null;
      if (data.lance_status[k] === "ok") {
        status_color = "green";
        actual_sum += v
      } else if (data.lance_status[k] === "waiting") {
        status_color = "yellow";
        theory_sum += v
      } else if (data.lance_status[k] === "did-not") {
        status_color = "red";
        owe_sum += v
      }
      $("#order-table").append($("<tr>")
        .append($("<td>")
          .text(k))
        .append($("<td>")
          .text(parseFloat(v).toFixed(2) + "$"))
        .append($("<td>")
          .append($("<p>")
            .attr("style", `color: ${status_color};`)
            .text(data.lance_status[k]))));

    });

    $("#money-sum").text(parseFloat(actual_sum).toFixed(2) + "$ + " + parseFloat(theory_sum).toFixed(2) + "$ + " + parseFloat(owe_sum).toFixed(2) + "$");
  });

});