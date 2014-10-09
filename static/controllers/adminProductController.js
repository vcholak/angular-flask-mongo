angular.module("sportsStoreAdmin")
.constant("productUrl", "/product/")
.config(function($httpProvider) {
    $httpProvider.defaults.withCredentials = true;
})
.controller("productCtrl", function ($scope, $resource, productUrl) {

    $scope.productsResource = $resource(productUrl + ":id", { id: "@id" }, {query: {isArray: false}});

    $scope.listProducts = function () {        
        $scope.products = $scope.productsResource.query();
        $scope.products.$promise.then(function(data) {
            $scope.products = data.products;
        });            
    }

    $scope.deleteProduct = function (product) {
        //product.$delete() - cannot use because product is not Resource but Object
        $scope.productsResource.delete(product).$promise.then(function () {
            $scope.products.splice($scope.products.indexOf(product), 1);
        });
    }

    $scope.createProduct = function (product) {
        new $scope.productsResource(product).$save().then(function (newProduct) {
            $scope.products.push(newProduct);
            $scope.editedProduct = null;
        });
    }

    $scope.updateProduct = function (product) {
        //product.$save(); - cannot use because product is not Resource but Object
        $scope.productsResource.save(product).$promise.then(function () {
            $scope.editedProduct = null;
        });
    }

    $scope.startEdit = function (product) {
        $scope.editedProduct = product;
    }

    $scope.cancelEdit = function () {
        $scope.editedProduct = null;
    }

    $scope.listProducts();
});
