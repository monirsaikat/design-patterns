<?php

namespace Strategy\Php;

final class ShippingQuote
{
    public function __construct(
        public float $cost,
        public int $etaDays,
        /** @var array<string, mixed> */
        public array $breakdown = []
    ) {}

    public function __toString(): string
    {
        $b = $this->breakdown ? json_encode($this->breakdown, JSON_PRETTY_PRINT) : '{}';
        return "Cost: {$this->cost}, ETA: {$this->etaDays} days\nBreakdown: {$b}\n";
    }
}