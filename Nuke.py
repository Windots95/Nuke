import ctypes
from ctypes import wintypes
import random
import time
import sys
import winsound
import math

# Windows API Setup
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
kernel32 = ctypes.windll.kernel32

def minimize_console():
    hWnd = kernel32.GetConsoleWindow()
    if hWnd:
        user32.ShowWindow(hWnd, 6)

def nuke_overload():
    minimize_console()
    sw = user32.GetSystemMetrics(0)
    sh = user32.GetSystemMetrics(1)
    start_time = time.time()
    
    print("!!! NUCLEAR OVERLOAD INITIALIZED !!!")
    print("Running 10 Stages of Desktop Destruction...")

    try:
        while True:
            elapsed = int(time.time() - start_time)
            stage = (elapsed // 10) % 10  # Switch every 10 seconds
            hdc = user32.GetDC(0)

            # --- LEGACY STAGES (V2 & V3) ---
            if stage == 0: # Jitter
                gdi32.BitBlt(hdc, random.randint(-5, 5), random.randint(-5, 5), sw, sh, hdc, 0, 0, 0xCC0020)
            
            elif stage == 1: # Pixel Melt
                x, y = random.randint(0, sw), random.randint(0, sh)
                gdi32.BitBlt(hdc, x+random.randint(-15, 15), y+random.randint(-15, 15), 300, 300, hdc, x, y, 0xCC0020)
            
            elif stage == 2: # 8-Bit Noise
                brush = gdi32.CreateSolidBrush(random.randint(0, 0xFFFFFF))
                rect = wintypes.RECT(random.randint(0, sw), random.randint(0, sh), random.randint(0, sw), random.randint(0, sh))
                user32.FillRect(hdc, ctypes.byref(rect), brush)
                gdi32.DeleteObject(brush)

            elif stage == 3: # Classic Spin
                pts = (wintypes.POINT * 3)(wintypes.POINT(30, 0), wintypes.POINT(sw, 30), wintypes.POINT(0, sh-30))
                gdi32.PlgBlt(hdc, ctypes.byref(pts), hdc, 0, 0, sw, sh, 0, 0, 0)

            elif stage == 4: # Psychedelic
                gdi32.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, 0x990066)

            # --- NEW STAGES (V5: The 5 New Effects) ---
            
            elif stage == 5: # EFFECT 1: THE GHOST TRAIL (Feedback Loop)
                # Copies the screen back onto itself with a slight scale and offset
                gdi32.StretchBlt(hdc, 5, 5, sw-10, sh-10, hdc, 0, 0, sw, sh, 0x8800C6) 
                if random.random() > 0.9: winsound.Beep(1200, 40)

            elif stage == 6: # EFFECT 2: VERTICAL SKEW (New Rotation Style)
                # Sharp diagonal tilting
                pts = (wintypes.POINT * 3)(
                    wintypes.POINT(random.randint(0, 100), 0), 
                    wintypes.POINT(sw - random.randint(0, 100), 50), 
                    wintypes.POINT(50, sh)
                )
                gdi32.PlgBlt(hdc, ctypes.byref(pts), hdc, 0, 0, sw, sh, 0, 0, 0)

            elif stage == 7: # EFFECT 3: DIGITAL RAIN (Column Shifts)
                col_x = random.randint(0, sw)
                gdi32.BitBlt(hdc, col_x, random.randint(-50, 50), 100, sh, hdc, col_x, 0, 0xCC0020)

            elif stage == 8: # EFFECT 4: THE ATOMIC SQUASH
                # Flattens the screen into a thin line and bounces it
                h_size = random.randint(10, sh)
                gdi32.StretchBlt(hdc, 0, random.randint(0, sh), sw, h_size, hdc, 0, 0, sw, sh, 0xCC0020)
                winsound.Beep(random.randint(200, 400), 20)

            elif stage == 9: # EFFECT 5: TUNNEL VISION (Circular Inversion)
                # Rapidly flashing center-focused inversions
                size = random.randint(100, 600)
                cx, cy = sw//2, sh//2
                rect = wintypes.RECT(cx-size, cy-size, cx+size, cy+size)
                user32.InvertRect(hdc, ctypes.byref(rect))
                # High pitched alarm beeps
                winsound.Beep(random.randint(3000, 4000), 30)

            user32.ReleaseDC(0, hdc)
            time.sleep(0.01) # Optimized for VM smoothness

    except KeyboardInterrupt:
        user32.InvalidateRect(0, None, True)
        print("\nNuke Aborted.")
        sys.exit()

if __name__ == "__main__":
    nuke_overload()