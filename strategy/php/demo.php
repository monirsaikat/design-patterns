<?php

use Strategy\Php\Order;
use Strategy\Php\ShippingContext;
use Strategy\Php\Strategies\DistanceBasedStrategy;
use Strategy\Php\Strategies\FlatRateStrategy;

spl_autoload_register(function ($class) {
    $baseDir = __DIR__ . '/';

    // convert namespace → file path
    $file = $baseDir . str_replace('Strategy\\Php\\', '', $class) . '.php';
    $file = str_replace('\\', '/', $file);

    if (file_exists($file)) {
        require $file;
    }
});

function line(): void { echo str_repeat('-', 60) . PHP_EOL; }

$order1 = new Order(
    subtotal: 1500,
    totalWeightKg: 6.5,
    destination: 'local',
    distanceKm: 12,
    express: true
);

$shippingContext = new ShippingContext(new FlatRateStrategy());
echo $shippingContext->quote($order1);

line();
$shippingContext->setStrategy(new DistanceBasedStrategy());
echo $shippingContext->quote($order1);