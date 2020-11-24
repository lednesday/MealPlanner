
///////////////////////recipe.html javascrip (recipe to add recipes)///////////////////////////////////
var counter_recipe_html = 0;//save the number of fields
function add_field_recipehtml() {
    counter_recipe_html++;

    var div = document.createElement ("div");
    div.id = "ingredient_diet";

    var label = document.createElement('label');
    label.innerHTML = " Item: ";
    label.htmlFor = "item"
    div.appendChild(label);
    var item_input = document.createElement('input');
    item_input.type = "text";
    item_input.name = "item";
    item_input.id = "item"+counter_recipe_html;
    div.appendChild(item_input);
    ingredients_field.appendChild(div);

    var label = document.createElement('label');
    label.innerHTML = " Quantity: ";
    label.htmlFor = "quantity"
    div.appendChild(label);
    var item_input = document.createElement('input');
    item_input.type = "text";
    item_input.name = "quantity";
    item_input.id = "quantity"+counter_recipe_html;
    div.appendChild(item_input);
    ingredients_field.appendChild(div);

    var label = document.createElement('label');
    label.innerHTML = " Units: ";
    label.htmlFor = "unit"
    div.appendChild(label);
    var item_input = document.createElement('input');
    item_input.type = "text";
    item_input.name = "unit";
    item_input.id = "unit"+counter_recipe_html;
    div.appendChild(item_input);
    ingredients_field.appendChild(div);
}

$('#button_add_field_recipe').click(function() {
  add_field_recipehtml();
});


/////////////////////////JS scripts for displayrecipe.html ////////////////////////
  function add_drop_list_recipe(array){
    var element = document.getElementById('select_name_recipe_droplist');

    while (element.hasChildNodes()) {
       element.removeChild(element.lastChild);
    }

    if (array.length > 0){

      for (i = 0; i < array.length; i++) {
        var option = document.createElement('option');
        option.value = array[i];
        option.innerHTML = array[i];
        element.appendChild(option);
      }

    }
    element.appendChild(option);
 };


 $('#select_recipe_mealplan_display').change(function() {
   var meal_plan = $("#select_recipe_mealplan_display").val();
   if(meal_plan != "")
   {

     $.getJSON( "/_view_recipes",
                {
                meal_plan:meal_plan},
                function(data) {
                  rsval = data.result.response;
                  if (rsval.length == 0){
                    rsval = ["No records found"]
                  }

                  add_drop_list_recipe(rsval)
                }
             );
   }

 });
///////////////////// CODES JS FOR cook_viewer.HTML //////////////////////

  function add_drop_list(array){
    var element = document.getElementById('select_generate_cooks');
    while (element.hasChildNodes()) {
       element.removeChild(element.lastChild);
    }

    if (array.length > 0){
      for (i = 0; i < array.length; i++) {
        var option = document.createElement('option');
        option.value = array[i];
        option.innerHTML = array[i];
        element.appendChild(option);
      }
    }
    element.appendChild(option);
 };

 $('#select_mealplan_viewer').change(function() {
   var meal_plan = $("#select_mealplan_viewer").val();
   console.log(meal_plan);
   if (meal_plan != "")
   {
     $.getJSON( "/_view_cooks",
                {
                meal_plan:meal_plan},
                function(data) {
                  rsval = data.result.response;
                  if (rsval.length == 0){
                    rsval = ["No records found"]
                  }
                  add_drop_list(rsval)
                }
             );
   }
 });

///////////////////////NEWPLAN.HTML/////////////////////////////////////
//signup page, checks the name is not already in database
$("#plan_name").keyup(function(event) {//function to check if a name is already in the database
   var txt = $("#plan_name").val();  // Current content of the input field
   var keycode = event.which;      // They key that just went up
   $.getJSON( "/_check_name",
              {text: txt},
              function(data) {
                rsval = data.result.response;
                console.log("rsval: " + rsval);
                if (rsval.localeCompare("Yes") == 0){
                    console.log("Hola")
                    $("#response").html("This name has been already taken. Choose another one")
                    disable("button")
                }
                else if (rsval.localeCompare("Zero") == 0){
                    $("#response").html("No name has been provided")
                    disable("button")
                }
                else{
                    $("#response").html("This name is available.");
                    enable("button")
                }
              }

           );
  });


  //add fields. list ranges is a list of dates where we need to select meals.
    function addFields(list_range){
        var number = list_range.length;

        while (container.hasChildNodes()) {
           container.removeChild(container.lastChild);
        }

        var start_date = $("#start_date").val();
        var end_date = $("#end_date").val();  // Curren

        for ( i = 0 ; i < number; i++){
          var fieldset = document.createElement ("fieldset");
          fieldset.setAttribute('class','box'+i);
          var legend = document.createElement ("legend");
          legend.innerHTML = "Select the meals you'll be sharing for " + list_range[i];
          var ul = document.createElement('ul')
          ul.setAttribute('class','checkbox');

          meals = ['Breakfast','Lunch','Snack','Dinner'];
          document.getElementById('container').appendChild(ul);
          var j = 0
          meals.forEach(fun_add);

          function fun_add(element, index, arr) {
            var li = document.createElement('li');
            var label = document.createElement('label');
            var input = document.createElement('input');
            input.type = "checkbox";
            input.name = "meal"+i;
            input.value = meals[j]
            j = j + 1;
            label.innerHTML = element;

            li.appendChild(label);
            li.appendChild(input);
            ul.appendChild(li);
          }

          fieldset.appendChild (ul);
          fieldset.appendChild (legend);
          container.appendChild(fieldset);
        }
   };

  function check_dates_order(){//checks that the start date is always before end date. Otherwise, it disable submit button.
      var start_date = $("#start_date").val();
      var end_date = $("#end_date").val();
      if (start_date > end_date){
        disable("button");
        $("#response").html("The start date cannot be after the end date.")
      }
      else if (start_date < end_date){
        $("#response").html("")
        enable("button");
      }
  };

  $("#start_date").change(range_fields);//events that check if user change dates
  $("#end_date").change(range_fields);

  function range_fields() {//gets start and end date and calculate how many days difference and print the same number of fields.
      var start_date = $("#start_date").val();
      var end_date = $("#end_date").val();  // Current content of the input field\

      $.getJSON( "/_count_inputs",
                {start: start_date,
                  end: end_date},
                 function(data) {
                   list_dates = data.result.dates_range;
                   addFields(list_dates);
                   check_dates_order();
                  }
        );
    };

  //
    function check_date_today(){//gets today's date and add it as default in start and end date, disable submit (to avoid send empty meal names and creates one field.)
      var date_today = new Date();
      var year = date_today.getFullYear();
      var month = String(date_today.getMonth() + 1).padStart(2, '0'); //January is 0!
      var day = String(date_today.getDate()).padStart(2, '0');
      date_today = year+'-'+ month+'-' + day;

      var element = document.getElementById('start_date');

      //If it isn't "undefined" and it isn't "null", then it exists.
      if(typeof(element) != 'undefined' && element != null){
        document.getElementById('start_date').value = date_today;
        document.getElementsByName("start_date")[0].setAttribute('min', date_today);//js prevent user to schedule a plan before today.
        document.getElementById('end_date').value = date_today;
        document.getElementsByName("end_date")[0].setAttribute('min', date_today);
        disable("button");
        range_fields();
      }
    }










//function to check if a name is already in the database of recipess
$("#recipe_name").keyup(function(event) {
   var meal_plan = $("#meal_plan").val();
   var recipe_name = $("#recipe_name").val();
   if (meal_plan!="")
   {
     var keycode = event.which;      // They key that just went up
     $.getJSON( "/_check_recipe",
                {recipe_name: recipe_name,
                meal_plan:meal_plan},
                function(data) {
                  rsval = data.result.response;
                  if (rsval.localeCompare("Yes") == 0){
                      $("#response").html("This name has been already taken. Choose another one");
                      disable("button_submit");
                  }
                  else if (rsval.localeCompare("Zero") == 0){
                      $("#response").html("No name has been provided");
                      disable("button_submit");
                  }
                  else{
                      $("#response").html("This name is available.");
                      enable("button_submit");
                  }
                }

             );
   }

  });

//function to check if a name is already in the database cooks
$("#cook_name").keyup(function(event) {
   var cook_name = $("#cook_name").val();
   var meal_plan = $("#meal_plan").val();
   // console.log(meal_plan);
   if (meal_plan!="")
   {
     var keycode = event.which;      // They key that just went up
     $.getJSON( "/_check_cook",
                {cook_name: cook_name,
                meal_plan:meal_plan},
                function(data) {
                  rsval = data.result.response;
                  if (rsval.localeCompare("Yes") == 0){
                      $("#response").html("This name has been already taken. Choose another one");
                      disable("button");
                  }
                  else if (rsval.localeCompare("Zero") == 0){
                      $("#response").html("No name has been provided");
                      disable("button");
                  }
                  else{
                      $("#response").html("This name is available.");
                      enable("button");
                  }
                }

             );
   }

  });

//function to check if a name is already in the databas cooks mails
  $("#cook_email").keyup(function(event) {
     var meal_plan = $("#meal_plan").val();
     var email = $("#cook_email").val();  // Current content of the input field
     if (meal_plan!="")
     {
       var keycode = event.which;      // They key that just went up
       $.getJSON( "/_check_email",
                  {meal_plan: meal_plan,
                  email: email},
                  function(data) {
                    rsval = data.result.response;
                    if (rsval.localeCompare("Yes") == 0){
                        $("#email_response").html("This email address have been already used");
                        disable("button");
                        console.log("Yes");
                    }
                    else if (rsval.localeCompare("No") == 0){
                        $("#email_response").html("")
                        enable("button");
                        console.log("No");

                    }
                  }

               );
     }

    });




// signup triggers event when selected one meal plan.
  $(document).ready(function(){
    $('#meal_plan').change(function(){
      $('#newplan').submit();
    });
  });

// signup triggers event when selected one meal plan.
  $(document).ready(function(){
    $('#recipe').change(function(){
      $('#recipe_meal').submit();
    });
  });

//for enabling and disable submit
  function disable(x) {//enable or disable submit
      document.getElementById(x).disabled = true;
  }
  function enable(x) {
      document.getElementById(x).disabled = false;
  }
