#!/bin/bash
echo "=== Starting Incident Response Drill ==="
echo ""

echo "[INCIDENT 1] Simulating high CPU usage..."
stress-ng --cpu 4 --timeout 60s --quiet &
STRESS_PID=$!
echo "CPU stress test running (PID: $STRESS_PID)"
sleep 60

echo ""
echo "[RESOLUTION 1] CPU stress test completed"
echo ""

echo "[INCIDENT 2] Generating application errors..."
for i in {1..50}; do
    curl -s http://localhost:8080/health > /dev/null
    sleep 0.1
done
echo "Check application logs: tail -n 20 ~/observability-lab/app.log"
echo "=== Incident Response Drill Complete ==="
