input_file = open('./inputs/aoc16.txt', 'r')
packet_input = input_file.read()

hex_table = {
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'A': '1010',
  'B': '1011',
  'C': '1100',
  'D': '1101',
  'E': '1110',
  'F': '1111'
}

def binary2int(bin):

  output = 0
  bin = bin[::-1]

  for i in range(len(bin)-1,-1,-1):
    output += int(bin[i])*2**i

  return output

version_sum = 0

class Packet():
  def __init__(self, packet_string):
    self.packet_string = packet_string
    self.version = binary2int(packet_string[:3])
    self.type = binary2int(packet_string[3:6])
    self.length_type = packet_string[6]
    self.length = 0
    self.value = 0
    self.subpackets = []

    packet_string = packet_string[6:]

    if self.type == 4:
      i = 0
      value = ''
      while i < len(packet_string):
        value += packet_string[i+1:i+5]
        i += 5
        if packet_string[i-5] == '0':
          break


      self.value = binary2int(''.join(value))
      self.length = 6 + i

    #packet contains subpackets
    else:
      packet_string = packet_string[1:]
      self.length = 7
      
      #len type 0
      if self.length_type == '0':
        self.length += 15
        sub_p_len = binary2int(packet_string[:15])
        packet_string = packet_string[15:]
        
        #find all subpackets
        all_packets_found = False
        packet_count = 0
        while all_packets_found is False:
          self.subpackets.append(Packet(packet_string))
          length = self.subpackets[packet_count].length
          self.length += length
          packet_string = packet_string[length:]
          packet_count += 1
          sub_p_len -= length
          if sub_p_len == 0:
            break

      #len type 1
      elif self.length_type == '1':
        self.length += 11
        sub_p_cnt = binary2int(packet_string[:11])
        packet_string = packet_string[11:]
        for i in range(sub_p_cnt):
          self.subpackets.append(Packet(packet_string))
          length = self.subpackets[i].length
          self.length += length
          packet_string = packet_string[length:]

  def print_version(self):
    sum = self.version
    for packet in self.subpackets:
      version_sum = packet.print_version()
      sum += version_sum
    return sum

  def set_values(self):
    if len(self.subpackets) == 0:
      pass
    else:
      for packet in self.subpackets:
        packet.set_values()

      if self.type == 0:
        for packet in self.subpackets:
          self.value += packet.value
      elif self.type == 1:
        self.value = 1
        for packet in self.subpackets:
          self.value *= packet.value
      elif self.type == 2:
        self.value = self.subpackets[0].value
        for packet in self.subpackets:
          if packet.value < self.value:
            self.value = packet.value
      elif self.type == 3:
        self.value = self.subpackets[0].value
        for packet in self.subpackets:
          if packet.value > self.value:
            self.value = packet.value
      elif self.type == 5:
        self.value = 1 if self.subpackets[0].value > self.subpackets[1].value else 0
      elif self.type == 6:
        self.value = 1 if self.subpackets[0].value < self.subpackets[1].value else 0
      elif self.type == 7:
        self.value = 1 if self.subpackets[0].value == self.subpackets[1].value else 0

packet_input = ''.join([hex_table[c] for c in packet_input])

packet = Packet(packet_input)
print(packet.print_version())
packet.set_values()
print(packet.value)