


$("document").ready(function(){









var ToggleMobileNavidationDropdown = function(event){
		$("#mobileNavigationDropdownContent").slideToggle( 200 , function(){} );

};
	$("#mobile-navigation-dropdown-toggler").on("click" , ToggleMobileNavidationDropdown );

	$("#mobileNavigationDropdownContent").hide();


});

