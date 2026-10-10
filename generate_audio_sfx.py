#!/usr/bin/env python3
"""
Generates procedural 16-bit PCM WAV sound effects for C&C Generals: Shinobi Wars mod.
Uses only Python standard library (wave, math, struct, random).
"""
import wave
import math
import struct
import random
import os

SAMPLE_RATE = 22050  # Classic Generals sample rate

def write_wav(filename, samples):
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        raw = bytearray()
        for s in samples:
            val = int(max(-1.0, min(1.0, s)) * 32767)
            raw.extend(struct.pack('<h', val))
        wf.writeframes(raw)
    print(f"Generated: {os.path.basename(filename)} ({len(samples)/SAMPLE_RATE:.2f}s)")

def make_chidori():
    # Electrical arc: high frequencyFM + sharp crackles
    dur = 1.2
    n = int(SAMPLE_RATE * dur)
    samples = []
    for i in range(n):
        t = i / SAMPLE_RATE
        env = min(1.0, t * 10) * max(0.0, 1.0 - t / dur)
        freq = 1200 + 800 * math.sin(2 * math.pi * 35 * t)
        sine = math.sin(2 * math.pi * freq * t)
        noise = (random.random() * 2 - 1) * 0.4
        samples.append((sine * 0.6 + noise) * env)
    return samples

def make_poof():
    # Smoke puff / replacement technique
    dur = 0.5
    n = int(SAMPLE_RATE * dur)
    samples = []
    for i in range(n):
        t = i / SAMPLE_RATE
        env = math.exp(-t * 9)
        noise = (random.random() * 2 - 1)
        samples.append(noise * env * 0.9)
    return samples

def make_fireball():
    # Low frequency rumble + flame roar
    dur = 1.8
    n = int(SAMPLE_RATE * dur)
    samples = []
    for i in range(n):
        t = i / SAMPLE_RATE
        env = min(1.0, t * 5) * max(0.0, 1.0 - (t / dur)**1.5)
        rumble = math.sin(2 * math.pi * 65 * t)
        noise = (random.random() * 2 - 1) * 0.7
        samples.append((rumble * 0.5 + noise * 0.5) * env)
    return samples

def make_explosion():
    # Punchy detonate
    dur = 1.2
    n = int(SAMPLE_RATE * dur)
    samples = []
    for i in range(n):
        t = i / SAMPLE_RATE
        env = math.exp(-t * 5)
        sub = math.sin(2 * math.pi * 45 * t) * math.exp(-t * 3)
        noise = (random.random() * 2 - 1)
        samples.append((sub * 0.6 + noise * 0.7) * env)
    return samples

def make_kunai_slice():
    # Metal swoosh
    dur = 0.25
    n = int(SAMPLE_RATE * dur)
    samples = []
    for i in range(n):
        t = i / SAMPLE_RATE
        env = math.sin(math.pi * (t / dur))
        freq = 2500 - 1500 * (t / dur)
        s = math.sin(2 * math.pi * freq * t)
        samples.append(s * env * 0.7)
    return samples

def make_puppet_clicks():
    # Wood gear clicks
    dur = 0.7
    n = int(SAMPLE_RATE * dur)
    samples = [0.0] * n
    for click in range(8):
        pos = int(click * (n / 8))
        for j in range(min(400, n - pos)):
            t = j / SAMPLE_RATE
            env = math.exp(-j / 40.0)
            val = math.sin(2 * math.pi * 1400 * t) * env * 0.6
            samples[pos + j] += val
    return samples

def make_water_cannon():
    # Heavy splash cannon
    dur = 1.6
    n = int(SAMPLE_RATE * dur)
    samples = []
    for i in range(n):
        t = i / SAMPLE_RATE
        env = min(1.0, t * 15) * math.exp(-t * 2.5)
        sub = math.sin(2 * math.pi * 50 * t)
        splash = (random.random() * 2 - 1) * (0.8 - 0.4 * (t/dur))
        samples.append((sub * 0.5 + splash * 0.5) * env)
    return samples

def make_chime():
    # Mystical scroll unseal
    dur = 1.4
    n = int(SAMPLE_RATE * dur)
    samples = []
    for i in range(n):
        t = i / SAMPLE_RATE
        env = math.exp(-t * 2.5)
        h1 = math.sin(2 * math.pi * 880 * t)
        h2 = math.sin(2 * math.pi * 1320 * t) * 0.5
        h3 = math.sin(2 * math.pi * 1760 * t) * 0.3
        samples.append((h1 + h2 + h3) * env * 0.5)
    return samples

def main():
    out_dir = os.path.join(os.path.dirname(__file__), 'Audio')
    os.makedirs(out_dir, exist_ok=True)
    
    effects = {
        'snd_chidori_spark.wav': make_chidori(),
        'snd_kage_bunshin.wav': make_poof(),
        'snd_kuchiyose_poof.wav': make_poof(),
        'snd_katon_goukakyu.wav': make_fireball(),
        'snd_paper_bomb_detonate.wav': make_explosion(),
        'snd_sabaku_sousou.wav': make_explosion(),
        'snd_shinra_tensei.wav': make_explosion(),
        'snd_kunai_throw1.wav': make_kunai_slice(),
        'snd_paper_bomb_fuse.wav': make_chidori(),
        'snd_puppet_clicks.wav': make_puppet_clicks(),
        'snd_giant_toad_water.wav': make_water_cannon(),
        'snd_scroll_stamp.wav': make_poof(),
        'snd_forbidden_scroll_unseal.wav': make_chime(),
    }
    
    for fname, data in effects.items():
        write_wav(os.path.join(out_dir, fname), data)

if __name__ == '__main__':
    main()
