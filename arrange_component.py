from component import *

def arrange_circuit(list_resistor, resistance):
    num_resistors = len(list_resistor)
    if (num_resistors == 0):
        return None
    
    if num_resistors == 1:
        current_resistor = list_resistor[0]
        if current_resistor.calculate_magnitude() == resistance:
            return current_resistor
        else: 
            return None  
    
    for i in range(len(list_resistor)):
        current_resistor = list_resistor[i]
        current_resistor_magnitude = current_resistor.calculate_magnitude()
        tail_resistor = list_resistor[0:i] + list_resistor[i+1:]
        # if current resistor connected series with the rest
        tail_target_series = resistance - current_resistor_magnitude
        if not tail_target_series < 0 :
            tail_result = arrange_circuit(tail_resistor, tail_target_series)
            if tail_result is not None: 
                return SeriesCircuit([current_resistor, tail_result])
        
        # if current resistor connected paralel with the rest
        divisor = current_resistor_magnitude - resistance
        if (divisor > 0):
            tail_target_paralel = resistance*current_resistor_magnitude/divisor
            tail_result = arrange_circuit(tail_resistor, tail_target_paralel)
            if tail_result is not None: 
                return ParalelCircuit([current_resistor, tail_result])
            
        # if current resistor excluded 
        tail_result = arrange_circuit(tail_resistor, resistance)
        if tail_result is not None:
            return tail_result
        
def arrange_circuit_with_memo(list_resistor, resistance, memo={}):
    key = (tuple(list_resistor), resistance)
    if key in memo:
        return memo[key]
    
    num_resistors = len(list_resistor)
    if (num_resistors == 0):
        return None
    
    if num_resistors == 1:
        current_resistor = list_resistor[0]
        if current_resistor.calculate_magnitude() == resistance:
            memo[key] = current_resistor
            return current_resistor
        else: 
            return None                
    
    for i in range(len(list_resistor)):
        current_resistor = list_resistor[i]
        current_resistor_magnitude = current_resistor.calculate_magnitude()
        tail_resistor = list_resistor[0:i] + list_resistor[i+1:]
        # if current resistor connected series with the rest
        tail_target_series = resistance - current_resistor_magnitude
        if not tail_target_series < 0 :
            tail_result = arrange_circuit_with_memo(tail_resistor, tail_target_series, memo)
            if tail_result is not None: 
                result = SeriesCircuit([current_resistor, tail_result])
                memo[key] = result
                return result
        # if current resistor connected paralel with the rest
        divisor = current_resistor_magnitude - resistance
        if (divisor > 0):
            tail_target_paralel = resistance*current_resistor_magnitude/divisor
            tail_result = arrange_circuit_with_memo(tail_resistor, tail_target_paralel, memo)
            if tail_result is not None: 
                result =  ParalelCircuit([current_resistor, tail_result])
                memo[key] = result
                return result
        # if current resistor excluded 
        tail_result = arrange_circuit_with_memo(tail_resistor, resistance, memo)
        if tail_result is not None:
            memo[key] = tail_result
            return tail_result
    
    memo[key] = None
    return None