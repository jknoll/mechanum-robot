# Xbox Wireless Controller Setup on Raspberry Pi for Robot Control

This guide explains how to configure an Xbox Wireless Controller with a Raspberry Pi running Raspberry Pi OS so that the controller is reliably connected via Bluetooth and produces input events that persist across reboots.

---

## ✅ Prerequisites

- Raspberry Pi 4 or newer with built-in Bluetooth
- Xbox Wireless Controller with Bluetooth support (Xbox One S or newer)
- Raspberry Pi OS with internet access

---

## 🧰 Required Packages

Install the necessary packages:

```bash
sudo apt update
sudo apt install bluetooth bluez joystick
```

---

## 🎮 Step 1: Install xpadneo Driver (Enhanced Bluetooth Support)

Install the enhanced Bluetooth driver for Xbox controllers:

```bash
sudo apt install dkms git
git clone https://github.com/atar-axis/xpadneo.git
cd xpadneo
sudo ./install.sh
```

Reboot after installation:

```bash
sudo reboot
```

---

## 🔌 Step 2: Load Required Input Modules

Ensure the `uinput` and `joydev` modules are loaded:

```bash
sudo modprobe uinput
sudo modprobe joydev
```

To make `uinput` load on boot:

```bash
echo uinput | sudo tee -a /etc/modules
```

---

## 🔄 Step 3: Pair and Trust the Controller

1. Put the controller into pairing mode by holding the pairing button until the Xbox logo flashes rapidly.
2. Launch the Bluetooth CLI:

```bash
bluetoothctl
```

Then enter the following commands:

```bash
power on
agent on
default-agent
scan on
```

Once you see your controller (e.g., `Xbox Wireless Controller`), use its MAC address:

```bash
pair XX:XX:XX:XX:XX:XX
trust XX:XX:XX:XX:XX:XX
connect XX:XX:XX:XX:XX:XX
```

Replace `XX:XX:XX:XX:XX:XX` with your controller's MAC address.

---

## 📶 Step 4: Verify Input Device

To confirm that the controller input is being received:

```bash
sudo evtest
```

You should see a device like `/dev/input/eventX: Xbox Wireless Controller`. Select it, and press buttons on the controller to verify input.

---

## 🔁 Step 5: Make It Persistent Across Reboots

- Bluetooth auto-connect is enabled by trusting the device (`trust` step above).
- `uinput` is configured to load at boot.
- The controller should now reconnect automatically when powered on.

---

## ⚠️ Appendix A: Detecting and Updating Outdated Controller Firmware

If your controller disconnects immediately after "Connection successful" or does not appear in `evtest`, you may be using an outdated firmware version (e.g., v5.09). This version is known to have compatibility issues with the Linux Bluetooth stack.

### 🔧 How to Update

1. Connect your controller to a **Windows 10/11** PC via USB or Bluetooth.
2. Open the [**Xbox Accessories App**](https://www.microsoft.com/store/productId/9NBLGGH30XJ3).
3. Follow the prompt to **update your controller firmware**.
4. After updating, repeat the pairing steps in this guide.

