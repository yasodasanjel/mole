<!doctype html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang=""> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8" lang=""> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9" lang=""> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang=""> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>Dashboard</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="apple-touch-icon" href="apple-touch-icon.png">
        <link rel="stylesheet" href="assets/css/style.css">
		<script src="assets/js/vendor/modernizr-2.8.3-respond-1.4.2.min.js"></script>
		<link href="https://fonts.googleapis.com/css?family=Ek+Mukta:200,300,400,500,600,700,800&amp;subset=devanagari,latin-ext" rel="stylesheet">
    </head>
    <body>
        <?php require_once('app-header.php');?>
		
		<!--Main Content Area Starts-->
		<section id="app-section">
			<ol class="breadcrumb no-margin margin-top-lg">
			  <li><a href="index.php">गृह पृष्ठ</a></li>
			  <li><a href="page-office.php">वैदेशिक रोजगार विभाग</a></li>
			  <li class="active">वार्षिक/ चौमासिक लक्ष्य</li>
			</ol>
			<div class="bg-white padding margin-top-lg">
				<div class="app-page-header">
					<div class="row">
						<div class="col-md-5">
							<h4>वार्षिक/ चौमासिक लक्ष्य</h4>
						</div>
						<div class="col-md-2">
							<select class="form-control input-sm">
							  <option>10</option>
							  <option>20</option>
							  <option>30</option>
							  <option>40</option>
							  <option>50</option>
							</select>
						</div>
						<div class="col-md-5">
							<div class="action-holder">
								<a href="#" title="" class="btn btn-xs btn-default"><i class="fa fa-file-code-o"></i> CSV</a>
								<a href="#" title="" class="btn btn-xs btn-default"><i class="fa fa-file-excel-o"></i> Excel</a>
								<a href="#" title="" class="btn btn-xs btn-default"><i class="fa fa-file-pdf-o"></i> PDF</a>
								<a href="#" title="" class="btn btn-xs btn-default"><i class="fa fa-print"></i> Print</a>
								<a href="add-budget.php" title="" class="btn btn-xs btn-success"><i class="fa fa-money"></i> Budget</a>
							</div>
						</div>
					</div>
				</div>
				<div class="table-responsive">
					<table class="table table-bordered table-hover">
						<thead>
							<tr>
								<th rowspan="2">क्र. म.</th>
								<th rowspan="2">कार्य विवरण</th>
								<th colspan="3">वार्षिक लक्ष्य</th>
								<th rowspan="2">थप्नुहोस</th>
							</tr>
							<tr>
								<th>परिमाण</th>
								<th>भार</th>
								<th>बजेट</th>
							</tr>
						</thead>
						<tbody>
							
							<tr>
								<td>१.</td>
								<td>सिप मुलक तालिम </td>
								<td>स्वरोजगार</td>
								<td>शुन्य</td>
								<td>50,000</td>
								<td><a href="add-program.php" title="" class="btn btn-xs btn-primary"><i class="fa fa-plus"></i></a></td>
							</tr>
							<tr>
								<td>१.</td>
								<td>युवा स्वरोजगार तालिम </td>
								<td>स्वरोजगार</td>
								<td>शुन्य</td>
								<td>100,000</td>
								<td><a href="add-program.php" title="" class="btn btn-xs btn-primary"><i class="fa fa-plus"></i></a></td>
							</tr>
							<tr>
								<td>१.</td>
								<td>अभिमुखी तालिम </td>
								<td>स्वरोजगार</td>
								<td>शुन्य</td>
								<td>100,000</td>
								<td><a href="add-program.php" title="" class="btn btn-xs btn-primary"><i class="fa fa-plus"></i></a></td>
							</tr>
							
						</tbody>
					</table>
				</div>
				<nav aria-label="Page navigation">
					<ul class="pagination">
						<li>
							<a href="#" aria-label="Previous">
								<span aria-hidden="true">&laquo;</span>
							</a>
						</li>
						<li><a href="#">1</a></li>
						<li><a href="#">2</a></li>
						<li><a href="#">3</a></li>
						<li><a href="#">4</a></li>
						<li><a href="#">5</a></li>
						<li>
							<a href="#" aria-label="Next">
								<span aria-hidden="true">&raquo;</span>
							</a>
						</li>
					</ul>
				</nav>
			</div>
		</section>
		<div class="clearfix"></div>
		<!--Main Content Area Ends-->
		
		<?php require_once('app-footer.php');?>
		
        <!-- Google Analytics: change UA-XXXXX-X to be your site's ID. -->
        <!--<script>
            (function(b,o,i,l,e,r){b.GoogleAnalyticsObject=l;b[l]||(b[l]=
            function(){(b[l].q=b[l].q||[]).push(arguments)});b[l].l=+new Date;
            e=o.createElement(i);r=o.getElementsByTagName(i)[0];
            e.src='//www.google-analytics.com/analytics.js';
            r.parentNode.insertBefore(e,r)}(window,document,'script','ga'));
            ga('create','UA-XXXXX-X','auto');ga('send','pageview');
        </script>-->
    </body>
</html>
