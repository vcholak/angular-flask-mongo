angular.module("sportsStoreAdmin")
.constant("authUrl", "/login")
.constant("logoutUrl", "/logout")
.constant("ordersUrl", "/order")
.controller("authCtrl", function ($scope, $http, $location, authUrl) {

    // withCredentials: true - this enables support for cross-origin requests ???
    $scope.authenticate = function (user, pass) {
        $http.post(authUrl, {
            username: user,
            password: pass
        }, {
            withCredentials: true
        }).success(function (data) {
            if (data.success) {
                $location.path("/main");
            } else {
                $scope.authenticationError = data;
            }                      
        }).error(function (error) {
            $scope.authenticationError = error;
        });
    }       
})
.controller("mainCtrl", function ($scope, $http, $location, logoutUrl) {

    $scope.screens = ["Products", "Orders"];
    $scope.current = $scope.screens[0];

    $scope.setScreen = function (index) {
        $scope.current = $scope.screens[index];
    };

    $scope.getScreen = function () {
        return $scope.current == "Products"
            ? "/views/adminProducts.html" : "/views/adminOrders.html";
    };
    
    $scope.logout = function() {
        $http.get(logoutUrl).success(function (data) { $location.path("/login"); });
    }
})
.controller("ordersCtrl", function ($scope, $http, ordersUrl) {

    $http.get(ordersUrl, { withCredentials: true })
        .success(function (data) {
            $scope.orders = data.orders;            
        })
        .error(function (error) {
            $scope.error = error;
        });

    //$scope.selectedOrder; //TODO for what?

    $scope.selectOrder = function (order) {
        $scope.selectedOrder = order;
    };

    $scope.calcTotal = function (order) {
        var total = 0;
        for (var i = 0; i < order.products.length; i++) {
            total +=
                order.products[i].count * order.products[i].price;
        }
        return total;
    }
});
