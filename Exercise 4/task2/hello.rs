fn update_string(input: String) -> String{
    let mut return_string = String::new();
    let input_vec: Vec<char>  = input.chars().collect();
    for c in input_vec {
        match c{
            '&' => return_string+="&amp;",
            '>' => return_string+="&gt;",
            '<' => return_string+="&lt;",
            _ => return_string.push(c)
        }
    }
    return return_string;
}

fn main(){
    let mut line = String::new();
    println!("Enter input:");
    std::io::stdin().read_line(&mut line).unwrap();
    let result = update_string(line);
    println!("Result: \n{}",result);
}   
