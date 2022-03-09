bargar=document.querySelector('.bargar')
navbar=document.querySelector('.navbar')
navlist=document.querySelector('.nav-list')
rightnav=document.querySelector('.rightnav')

bargar.addEventListener('click',()=>{
    navbar.classlist.toggle('v-class-resp');
    navlist.classlist.toggle('v-class-resp');
    navbar.classlist.toggle('h-nav-resp');
})