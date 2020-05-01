function modeStyleSet(btnSelected, btnNotSelected1, btnNotSelected2, btnNotSelected3) {
    btnSelected.style.textShadow = '0 0 7px #a5ebd1';
    btnSelected.style.backgroundColor = '#161714';
    btnSelected.style.color = 'white';
    btnSelected.children[0].style.color = 'white';
    btnNotSelected1.style.textShadow = 'None';
    btnNotSelected1.style.backgroundColor = '#2e2f2a';
    btnNotSelected1.style.color = '#368e95';
    btnNotSelected1.children[0].style.color = '#27666b';
    btnNotSelected2.style.textShadow = 'None';
    btnNotSelected2.style.backgroundColor = '#2e2f2a';
    btnNotSelected2.style.color = '#368e95';
    btnNotSelected2.children[0].style.color = '#27666b';
    btnNotSelected3.style.textShadow = 'None';
    btnNotSelected3.style.backgroundColor = '#2e2f2a';
    btnNotSelected3.style.color = '#368e95';
    btnNotSelected3.children[0].style.color = '#27666b';
}

function controllerStyleSet() {
    controllerBaseStyleSet();
    controllerOverlayStyleSet();
}

function controllerBaseStyleSet() {
    let overlaySelector = document.getElementsByClassName('leaflet-control-layers-base');
    let baseLabels = overlaySelector.item(0).children;
    let openStreetLabelInput = baseLabels[0].getElementsByTagName('input')[0];
    let openStreetLabelText = baseLabels[0].getElementsByTagName('span')[0];
    let satelliteLabelInput = baseLabels[1].getElementsByTagName('input')[0];
    let satelliteLabelText = baseLabels[1].getElementsByTagName('span')[0];
    addBaseLabelEvents(openStreetLabelInput,openStreetLabelText,satelliteLabelText);
    addBaseLabelEvents(satelliteLabelInput,satelliteLabelText,openStreetLabelText);
    if (openStreetLabelInput.checked === true) {
            openStreetLabelText.style.color = 'white';
            openStreetLabelText.style.textShadow = '0 0 7px #a5ebd1';
            satelliteLabelInput.style.color = '#b4ffda';
            satelliteLabelInput.style.textShadow = 'None';
        }
}

function addBaseLabelEvents(inputChecked,textChecked,textUnChecked) {
    inputChecked.addEventListener("click", function () {
        if (inputChecked.checked === true) {
            textChecked.style.color = 'white';
            textChecked.style.textShadow = '0 0 7px #a5ebd1';
            textUnChecked.style.color = '#b4ffda';
            textUnChecked.style.textShadow = 'None';
        }
    });
}

function controllerOverlayStyleSet() {
    let overlaySelector = document.getElementsByClassName('leaflet-control-layers-overlays');
    let OverlayLabels = overlaySelector.item(0).children;
    for (let i = 0; i < OverlayLabels.length; i++) {
        let BaseInput = OverlayLabels[i].getElementsByTagName('input')[0];
        let BaseText = OverlayLabels[i].getElementsByTagName('span')[0];
        BaseInput.addEventListener("click", function () {
            if (BaseInput.checked === true) {
                BaseText.style.color = 'white';
                BaseText.style.textShadow = '0 0 7px #a5ebd1';
            } else {
                BaseText.style.color = '#b4ffda';
                BaseText.style.textShadow = 'None';
            }
        });
        if (BaseInput.checked === true) {
            BaseText.style.color = 'white';
            BaseText.style.textShadow = '0 0 7px #a5ebd1';
        } else {
            BaseText.style.color = '#b4ffda';
            BaseText.style.textShadow = 'None';
        }
    }
}