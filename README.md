# pifan

A Raspberry Pi CPU temperature monitoring service with REST API.

## Installation

1. Copy the service file to systemd directory:
```bash
sudo cp pifan.service /etc/systemd/system/
```

2. Reload systemd to recognize the new service:
```bash
sudo systemctl daemon-reload
```

3. Enable the service to start on boot:
```bash
sudo systemctl enable pifan
```

4. Start the service:
```bash
sudo systemctl start pifan
```

## Service Management

- Check service status:
```bash
sudo systemctl status pifan
```

- Stop the service:
```bash
sudo systemctl stop pifan
```

- Restart the service:
```bash
sudo systemctl restart pifan
```

## API Endpoints

- `GET /`: API documentation
- `GET /temperature`: Get current CPU temperature in Celsius

## Logs

View service logs:
```bash
sudo journalctl -u pifan -f
```
