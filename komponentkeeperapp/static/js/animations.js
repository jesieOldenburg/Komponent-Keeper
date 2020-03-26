console.log('animations is here');
let addComponentButton = document.querySelector('#add-component-button')


/*
1. When we mouse over, the bounce class is REMOVED
2. Then the heartbeat class is ADDED
*/ 

addComponentButton.addEventListener('mouseover', (e) =>{
    console.log('You Hovered');
    // Remove the initial Class from the node
    addComponentButton.classList.remove('bounceIn')
    addComponentButton.classList.add('heartBeat')
    // void addComponentButton.offsetWidth
})
/*
3. Then the mouseout clones the Button
    a. The class will still be heartbeat
*/ 

addComponentButton.addEventListener('mouseout', (e) =>{
    let newButton = addComponentButton.cloneNode(true)
    console.log(newButton);
    addComponentButton.parentNode.replaceChild(newButton, addComponentButton)
    addComponentButton.classList.remove('bounceIn')
    addComponentButton.classList.add('heartBeat')
    // addComponentButton.classList.add('heartBeat')
})