function loginShowFunction() {
  var login_window = document.getElementById('login_window');
  var closing_area = document.getElementById('closing_area');
  if( !login_window.classList.contains('show_window') )
  {
    login_window.classList.add('show_window');
    closing_area.classList.add('show_area');
    login_window.classList.remove('hide_window');
    closing_area.classList.remove('hide_area');
    
  }  
}  

function loginHideFunction() {
  var login_window = document.getElementById('login_window');
  var closing_area = document.getElementById('closing_area');
  if( !login_window.classList.contains('hide_window') )
  {
    login_window.classList.add('hide_window');
    closing_area.classList.add('hide_area');
    login_window.classList.remove('show_window');
    closing_area.classList.remove('show_area');
  }  
}