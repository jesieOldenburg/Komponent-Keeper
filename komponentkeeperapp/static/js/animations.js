console.log('animations is here');
let addComponentButton = document.querySelector('#add-component-button')
let newButton = addComponentButton.cloneNode(true)
console.log(addComponentButton);

addComponentButton.addEventListener('mouseover', (e) =>{
    console.log('You Hovered');
    // Remove the initial Class from the node
    addComponentButton.classList.remove('bounceInRight')
    addComponentButton.classList.add('heartBeat')
})


addComponentButton.addEventListener('mouseout', (e)=>{
    addComponentButton.parentNode.replaceChild(newButton, addComponentButton)
    addComponentButton.classList.add('heartBeat')
})