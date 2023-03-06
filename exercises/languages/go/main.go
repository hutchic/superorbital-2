package main

import (
    "log"
    "os"

    "github.com/urfave/cli/v2"
)

func main() {
    app := &cli.App{
        Name:        "drone client cli",
        Description: "a cli for interacting with the drones api",
        Commands: []*cli.Command{
            {
                Name:    "create",
                Aliases: []string{"c"},
                Usage:   "create a drone",
                Flags: []cli.Flag{
                    &cli.StringFlag{
                        Name:     "file, f",
                        Usage:    "filename that contains json payload for creating drone",
                        Required: true,
                    },
                },
                Action: func(c *cli.Context) error {
                    fileName := c.String("file")
                    log.Printf("creating drone from file %v", fileName)
                    return nil
                },
            },
            {
                Name:    "list",
                Aliases: []string{"l"},
                Usage:   "list all drones",
                Action: func(c *cli.Context) error {
                    // TODO: add real API functionality
                    log.Println("listing drones")
                    return nil
                },
            },
        },
    }

    err := app.Run(os.Args)
    if err != nil {
        log.Fatal(err)
    }
}
