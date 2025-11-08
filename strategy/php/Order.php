<?php
declare(strict_types=1);

namespace Strategy\Php;

final class Order {
    public function __construct(
        public float $subtotal,      
        public float $totalWeightKg, 
        public string $destination,  
        public int $distanceKm,      
        public bool $express = false 
    ) {}
}