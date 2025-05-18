use std::fs;
use std::path::Path;
use std::process::Command;
use std::thread;
use std::time::{Duration, Instant};

// Discover all Python agent files (*.py) in the 'python_agents' folder
fn discover_agents() -> Vec<String> {
    let agent_dir = "python_agents";
    let mut agents = vec![];

    // Read directory entries
    if let Ok(entries) = fs::read_dir(agent_dir) {
        for entry in entries.flatten() {
            let path = entry.path();

            // Check file extension == ".py"
            if let Some(ext) = path.extension() {
                if ext == "py" {
                    if let Some(filename) = path.file_name() {
                        if let Some(name_str) = filename.to_str() {
                            agents.push(name_str.to_string());
                        }
                    }
                }
            }
        }
    } else {
        eprintln!("[ERROR] Could not read agent directory '{}'", agent_dir);
    }

    agents
}

// Runs a Python agent with retries and logs duration
fn run_agent_with_retries(agent_name: &str, max_retries: u8, retry_delay_secs: u64) {
    let agent_path = format!("python_agents/{}", agent_name);
    let mut attempts = 0;

    loop {
        attempts += 1;
        println!(
            "[RUNTIME] Attempt {} to run agent '{}'",
            attempts, agent_path
        );

        let start = Instant::now();

        let output = Command::new("python3")
            .arg("-u")
            .arg(&agent_path)
            .output()
            .expect("Failed to execute agent");

        let duration = start.elapsed();

        // Show stdout
        println!("{}", String::from_utf8_lossy(&output.stdout));

        // Show stderr
        if !output.stderr.is_empty() {
            eprintln!("[ERROR] {}", String::from_utf8_lossy(&output.stderr));
        }

        // If success, break
        if output.status.success() {
            println!(
                "[RUNTIME] Agent '{}' succeeded in {:.2?} on attempt {}",
                agent_name, duration, attempts
            );
            break;
        } else {
            println!(
                "[RUNTIME] Agent '{}' failed in {:.2?} with exit code {:?} (attempt {})",
                agent_name,
                duration,
                output.status.code(),
                attempts
            );

            if attempts >= max_retries {
                println!(
                    "[RUNTIME] Agent '{}' failed after {} attempts. Giving up.",
                    agent_name, max_retries
                );
                break;
            }

            println!(
                "[RUNTIME] Retrying agent '{}' after {}s...\n",
                agent_name, retry_delay_secs
            );
            thread::sleep(Duration::from_secs(retry_delay_secs));
        }
    }
}

fn main() {
    println!("[RUNTIME] Starting dynamic agent discovery runtime...");

    let agents = discover_agents();
    if agents.is_empty() {
        println!("[RUNTIME] No agents found.");
        return;
    }

    let max_retries = 3;
    let retry_delay_secs = 2;
    let mut handles = vec![];

    // Run each agent in its own thread
    for agent in agents {
        let agent_name = agent.to_string();

        let handle = thread::spawn(move || {
            run_agent_with_retries(&agent_name, max_retries, retry_delay_secs);
        });

        handles.push(handle);
    }

    // Wait for all threads to finish
    for handle in handles {
        handle.join().expect("Thread panicked");
    }

    println!("[RUNTIME] All agents have finished execution.");
}
