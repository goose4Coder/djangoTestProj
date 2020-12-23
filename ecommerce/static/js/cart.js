var updateBtns = document.querySelectorAll("button[data-action='add']");

console.log(updateBtns);
for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', function(event){
  console.log('ok');
  var productId = event.target.dataset.product;
  var action = event.target.dataset.action;
  console.log('productId:', productId, 'Action:', action);
  console.log('User:', user);

});
}
