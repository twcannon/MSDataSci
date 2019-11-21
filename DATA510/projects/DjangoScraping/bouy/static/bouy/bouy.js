function postBouy() {
    var myVariable = $("#input_name").val();
    console.log(myVariable);

    $.ajax(
        {
            type: "POST",
            data: { 
                myVariableKey: myVariable
            },
            success: function (returnedData) {
                // $("#btn_02").text(returnedData['places'][0]['place name'])
                // console.log(returnedData['places'][0]['place name'])       
            }
        }
    );

}