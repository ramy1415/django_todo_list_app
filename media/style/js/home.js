// changing item status to Active or Done when clicked
function item_clicked(btn,id,title) {
    
    $.ajax({
        url:`/togglestatus`,
        method:"GET",
        data:{'item_id':id,csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},
        dataType:"json",
        success:function(result){ 
            // if in the view all todos template
            if (title == 'All Items'){
                // getting this div children icon
                const icon_element = $($(btn).children('h1').children('i')[0])
                // changing this div children icon to checked icon and vice versa
                icon_element.toggleClass(['far','fas'])
            }else{
                // if in the view done or active todos template remove the element
                btn.remove()
            }
            alert(result.message)
        },
        error:function(error){
            alert(error.responseJSON.message)
            }
        });
}

// getting new html element for the new added item
function get_item_element(id,item_description,title) {
    return $(`
            <div onclick="item_clicked(this,'${id}','${title}')">
                <h1> <i class="far fa-square"></i> ${item_description}</h1>
            </div>
            `)
}

// ajax function adding new todo item in database
function add_todo_item(event,title) {
    event.preventDefault()
    const item_description = document.getElementById('description').value
    $.ajax({
        url:`/additem`,
        method:"POST",
        data:{'description':item_description,csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},
        dataType:"json",
        success:function(result){ 
            const {id} = result
            const new_item = get_item_element(id,item_description,title)
            $('.items').append(new_item)
            alert(result.message)
        },
        error:function(error){
            alert(error.responseJSON.message)
            }
        });

}