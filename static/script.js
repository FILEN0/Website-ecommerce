document.documentElement.style.setProperty('--text-colormode', 'black');
    document.documentElement.style.setProperty('--bg-colormode', '#eee');
    document.documentElement.style.setProperty('--filter-colormode',0);            
    document.documentElement.style.setProperty('--reverse-colormode','#222');
function Flipcolor(){    
    if(document.documentElement.style.getPropertyValue('--filter-colormode') == 1){
        document.documentElement.style.setProperty('--text-colormode', 'black');
        document.documentElement.style.setProperty('--bg-colormode', '#eee');
        document.documentElement.style.setProperty('--filter-colormode',0);            
        document.documentElement.style.setProperty('--reverse-colormode','#222');
    }else{
        document.documentElement.style.setProperty('--text-colormode', 'white');
        document.documentElement.style.setProperty('--bg-colormode', '#222');
        document.documentElement.style.setProperty('--filter-colormode',1);            
        document.documentElement.style.setProperty('--reverse-colormode','black');
    }
}
