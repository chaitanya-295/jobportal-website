// HireUp Platform Common Scripts

$(document).ready(function () {
    // This script can be used for common UI interactions.
    // Dashboard-specific table initializations are handled within their respective templates 
    // to maintain unique configurations (ordering, column counts, etc.)
    
    // Global Tooltip initialization for BS5
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl)
    })
});