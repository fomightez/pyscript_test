function getUrl() {
    const urlSearchParams = new URLSearchParams(window.location.search);
    const params = Object.fromEntries(urlSearchParams.entries());
    return params['url'] == null? './test_nb.ipynb' : params['url']
}

window.onload = function() { 
    window.nblite.openNbAsPyScript(getUrl(), 'nb-content')
};
  
