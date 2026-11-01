# Platform differences

*What's the same and what differs between the Android and macOS apps.*

Pottery Wheel is **one app on two platforms**. The design engine, file format, and export
are shared, so a project saved on one opens on the other. The differences are mostly in
how you interact with the interface.

<span class="badge android">Android</span> phone/tablet · touch
&nbsp;&nbsp;
<span class="badge macos">macOS</span> desktop · mouse & keyboard, menu bar

## Interaction

| Action | <span class="badge android">Android</span> | <span class="badge macos">macOS</span> |
|---|---|---|
| Select / move | tap & drag | click & drag |
| Scale a stamp | pinch or corner handles | corner handles |
| Rotate / pan view | two-finger gestures | drag + modifier / trackpad |
| Commands | on-screen buttons & bottom nav | **menu bar** (File, Edit, …) |
| Save | `Save` → system document dialog | ++cmd+s++ → save panel |

## What's shared

- The **JSON** project format — open a file saved on either platform.
- Templates, connections, galleries and lids.
- Stamps and reliefs, wrapped to the curved surface.
- STL export and casting-mold generation.

## What differs

=== "Android"
    - Adding a part opens a **connection dialog** to choose the attachment point.
    - The current **version** shows at the bottom-right of the nav bar.
    - Files use the system document picker; the suggested extension is `.json`.

=== "macOS"
    - Standard **menu bar** with File/Edit commands and keyboard shortcuts.
    - Closing the last window keeps the app running; **New/Open/New from Template** reopens one.
    - A **Help** menu link points to this guide.
    - The current **version** shows at the bottom-right of the nav bar.

!!! note "Feature parity"
    Features roll out across both apps. If something here appears on only one platform, it's
    either in progress or noted on the relevant page.
