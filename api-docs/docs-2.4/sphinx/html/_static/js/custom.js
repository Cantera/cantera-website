const updateCopyButtonImages = () => {
    const copybuttonimages = document.querySelectorAll('a.copybtn img')
    copybuttonimages.forEach((img, index) => {
    img.setAttribute('src', 'path-to-new-image.svg')
    })
}

runWhenDOMLoaded(updateCopyButtonImages)