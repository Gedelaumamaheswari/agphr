$( function() {   
  let wrapper1 = $('.field_wrapper1'); //Input field wrapper
  $(wrapper1).on('click', '.remove_button', function(e){
    e.preventDefault();
    $(this).parent('li').remove(); //Remove field html                      
  }); 
  $( "#id_skills1" ).autocomplete({
    source: '/skillSearch/',
    select: function( event, ui ) {  
      let fieldHTML1 = `<li class="list-group-item d-flex justify-content-between align-items-center"> 
                          <input type="hidden" id="${ui.item.label}" name="skills" value="${ui.item.id}">
                            <h6>
                              <span class="badge bg-success mx-1">${ui.item.label}</span>
                            </h6>
                            <a href="javascript:void(0);" class="remove_button">
                              <i class="fa fa-trash text-danger"></i>
                            </a>
                        </li>`; 
      if($(`span:contains(${ui.item.label})`).length<1)
      {
        $(wrapper1).append(fieldHTML1); //Add field html
      }
      this.value = "";
      return false;      
    }
  });
});