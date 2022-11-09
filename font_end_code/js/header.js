let count=0;

let changeMenuIcon= function(icon)
{
    
    icon.classList.toggle('gg-close');
    const menuItem=document.querySelector(".menuitem");
    if(count ==0){
   menuItem.style.margin='0%';
   count=1
    }
    else{
        menuItem.style.margin='0% 0% 0% -100%';
count=0;
    }
}