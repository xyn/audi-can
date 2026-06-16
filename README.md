# Python library that interacts with different parts of Audi vehicles over the CANbus

This library is mostly focused around the Audi A4 B6/B7 / A6 C5 / A3 8P era cars but may evolve with support for newer Audis in the future.

> **Note:**
> this is a hobby project and may never be complete, do not expect a bug-less experience.
> Expect broken features and sloppy code.

Main goal of this library is to interact with the car's cluster display, RNS-E radio and steering wheel controls to retrofit modern comfort features into the OEM hardware.

To-do list:
- RNS-E
  - [x] Enable / disable TV Mode
  - [x] Read buttons while in TV Mode
- MFSW
  - [ ] Read left-side scroll wheel & select
  - [ ] Read out "MODE" button in case the car has Telephony enabled
- Cluster
  - Support different cluster types
    - [ ] Red MFA
    - [ ] White MFA
    - [ ] Color MFA
  - [ ] Write custom text on the top two lines of the FIS
  - [ ] Draw custom data in the "navigation" portion of the DIS
  - [ ] (Ideally) control the entirey of the DIS to take advantage of the whole screen
