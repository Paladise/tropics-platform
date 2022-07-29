function delete_water(e) {
     if(!confirm('Delete this water?')){
          //prevent sending the request when user clicked 'Cancel'
          e.preventDefault();
     }
}