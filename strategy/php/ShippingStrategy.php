<?php
declare(strict_types=1);

namespace Strategy\Php;

interface ShippingStrategy
{
    public function name(): string;

    public function supports(Order $order): bool;

    public function validate(Order $order): void;

    public function quote(Order $order): ShippingQuote;
}