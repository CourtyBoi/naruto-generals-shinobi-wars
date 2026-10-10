#!/usr/bin/env python3
"""
C&C Generals / Zero Hour BIG File Packer
Packages the Data/ and Art/ folders into a single !!!NarutoShinobiWars.big file
"""
import os
import struct

def pack_big(source_dir, output_big_path):
    files_to_pack = []
    
    # Collect all files inside Data and Art
    for sub in ['Data', 'Art']:
        full_sub = os.path.join(source_dir, sub)
        if os.path.exists(full_sub):
            for root, _, files in os.walk(full_sub):
                for f in files:
                    full_path = os.path.join(root, f)
                    rel_path = os.path.relpath(full_path, source_dir).replace('/', '\\')
                    files_to_pack.append((rel_path, full_path))

    if not files_to_pack:
        print("No files found to pack.")
        return

    print(f"Packing {len(files_to_pack)} files into {output_big_path}...")

    # Calculate header size
    # BIG4 header: 4 bytes magic ('BIG4'), 4 bytes total size, 4 bytes num_files (Big-Endian), 4 bytes header_size (Big-Endian)
    header_entries = bytearray()
    for rel_path, full_path in files_to_pack:
        # Each entry: 4 bytes offset (Big-Endian), 4 bytes size (Big-Endian), null-terminated filename
        name_bytes = rel_path.encode('latin1') + b'\x00'
        # Dummy offset for now (will calculate below)
        header_entries.extend(struct.pack('>II', 0, os.path.getsize(full_path)) + name_bytes)

    header_size = 16 + len(header_entries)
    current_offset = header_size

    # Re-calculate correct offsets
    final_header = bytearray()
    for rel_path, full_path in files_to_pack:
        file_size = os.path.getsize(full_path)
        name_bytes = rel_path.encode('latin1') + b'\x00'
        final_header.extend(struct.pack('>II', current_offset, file_size) + name_bytes)
        current_offset += file_size

    total_archive_size = current_offset

    # Write BIG archive
    with open(output_big_path, 'wb') as out:
        out.write(b'BIG4')
        out.write(struct.pack('<I', total_archive_size))          # Little-endian total file size
        out.write(struct.pack('>I', len(files_to_pack)))          # Big-endian entry count
        out.write(struct.pack('>I', header_size))                 # Big-endian header size
        out.write(final_header)

        # Write actual file contents
        for _, full_path in files_to_pack:
            with open(full_path, 'rb') as f:
                out.write(f.read())

    print(f"Successfully created {output_big_path} ({os.path.getsize(output_big_path)} bytes)")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "!!!NarutoShinobiWars.big")
    pack_big(base_dir, output_path)
