// this adds the active class to the current page's link in the nav
window.onload = function () {
    let current_page = document.getElementsByClassName(location.pathname);
    console.log(current_page)
    for (let item of current_page) {
       item.classList.add("uk-active")
    }
};